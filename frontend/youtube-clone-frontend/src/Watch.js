import React, { Component } from "react";
import InfiniteScroll from 'react-infinite-scroll-component';
import './watch.scss'
import {abbreviate_number} from './helpers'
import VideoPreview from "./VideoPreview";

class Watch extends Component {

    constructor(props) {
        super(props);

        const urlParams = new URLSearchParams(props.location.search);

        this.state = {
            'manifest_url': "",
            'title': "",
            'channel': "",
            "channel_url": "",
            "channel_icon_url": "",
            "view_count": "",
            "upload_date": "",
            "subscriber_count": "",
            "description": "",
            items: [],
            comments: [],
            hasMore: false,
            commentValue: "",
            video_id: urlParams.get('id')
        }

        this.new_page(props);

        this.handleCommentSubmit = this.handleCommentSubmit.bind(this);
        this.handleCommentChange = this.handleCommentChange.bind(this);
        
    }

    componentDidMount() {
        var submit_comment = document.getElementById("submit-comment");
        document.getElementById("comment-box").oninput = function(e) {
            console.log(e.target.value);
            if (e.target.value.length > 0) {
                submit_comment.disabled = false;
            } else {
                submit_comment.disabled = true;
            }
        }
    }

    componentWillReceiveProps(nextProps) {
        if (this.props.location.search != nextProps.location.search) {
            this.new_page(nextProps);
        }
    }

    new_page(props) {
        const urlParams = new URLSearchParams(props.location.search);
        const id = urlParams.get('id');

        this.setState({
            items: [],
            comments: [],
            video_id: id
        })

        fetch("/video?id="+id, {
        })
        .then(response => response.json())
        .then(data => {
            console.log(data["manifest_url"])
            this.setState({
                "manifest_url": data["manifest_url"]+"?x-request=html",
                "title": data["title"],
                "channel": data["channel"],
                "channel_url": data["channel_url"],
                "channel_icon_url": data["channel_icon_url"],
                "view_count": data["view_count"],
                "upload_date": data["upload_date"],
                //"subscriber_count": abbreviate_number(data["subscriber_count"]),
                "subscriber_count": data["subscriber_count"],
                "description": data["description"]
            })

            document.title = data["title"];

            var video = document.getElementById("videoPlayer");

            try {
                this.state.player.reset();
            } catch (error) {
                
            }
            this.state.player = window.dashjs.MediaPlayer().create();
            this.state.player.initialize(video, data["manifest_url"], true);
        })

        fetch("/upnext_videos?start=0&num=10", {
        })
        .then(response => response.json())
        .then(data => {
            this.setState({
                items: this.state.items.concat(data["videos"])
            })
        })

        fetch("/get_comments?start=0&num=10&video_id=" + id, {})
        .then(response => response.json())
        .then(data => {
            this.setState({
                comments: this.state.comments.concat(data["data"])
            })
        })
    }


    fetchMoreData = () => {
        fetch("/upnext_videos?start=0&num=5", {
        })
        .then(response => response.json())
        .then(data => {
            this.setState({
                items: this.state.items.concat(data["videos"])
            })
        })
      };

    handleSubscribe() {
    }

    handleCommentSubmit(event) {
        event.preventDefault();
        console.log("COMMENT SUBMIT")
        fetch("/submit_comment?video_id=" + this.state.video_id + "&content=" + this.state.commentValue, {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
    }

    handleCommentChange(event) {
        this.setState({commentValue: event.target.value});
    }

    render() {
        return <div class="watch-container">
        <div class="left">
            <video
            autoPlay=""
            id="videoPlayer"
            controls></video>
            <div class="under-video-area">
                <div class="video-description">
                    <div class="description-top">
                        <div class="title">{this.state.title}</div>
                        <div class="views_date">{this.state.view_count} views • {this.state.upload_date}</div>
                    </div>
                    <div class="description-bottom">
                        <div class="icon-container">
                            <img src="#"/>
                        </div>
                        <div class="channel-text">
                            <p class="channel-title">{this.state.channel}</p>
                            <p class="subscriber-count">{this.state.subscriber_count} subscribers</p>
                        </div>
                        <div class="subscribe-button-container">
                            <button onClick={this.handleSubscribe}>SUBSCRIBE</button>
                        </div>
                        <div class="description-text">
                            <p><pre>{this.state.description}</pre></p>
                        </div>
                        
                    </div>
                </div>
                <div class="comments-container">
                    <div class="comment-options">
                        <div class="comment-count">
                            {this.state.comments.length} {this.state.comments.length == 1 ? 'Comment' : 'Comments'}
                        </div>
                        <div>
                            Sort by:
                        </div>
                        <div>
                            <select>
                                <option>Top</option>
                                <option>New</option>
                            </select>
                        </div>
                    </div>
                    <div class="comment-input-container">
                        <form onSubmit={this.handleCommentSubmit}>
                            <input type="text" id="comment-box" name="comment" placeholder="Write a comment" onChange={this.handleCommentChange} value={this.state.commentValue} required/>
                            <button id="submit-comment" type="submit" value="Submit" disabled>COMMENT</button>
                        </form>
                    </div>
                    <div class="comments-list">
                        {this.state.comments.map((val) => (
                            <VideoComment 
                                username={val.username}
                                content={val.content}
                                post_time={val.post_time}
                            />
                        ))}
                    </div>
                </div>
            </div>
            
        </div>
        <div class="right">
            <div class="video-list-container" id="video-list-container">
                <InfiniteScroll
                dataLength={this.state.items.length}
                next={this.fetchMoreData}
                hasMore={true}
                scrollableTarget="video-list-container"
                loader={<h4>Loading...</h4>}>
                    {this.state.items.map((val) => (
                        <RecommendedvideoPreview 
                            title={val.title} 
                            view_count={val.view_count} 
                            upload_date={val.upload_date}
                            video_length={val.video_length}
                            static_url={val.static_url}
                            animated_url={val.animated_url}
                            channel={val.channel}
                            video_url={val.video_url}
                        />
                    ))}
                </InfiniteScroll>
            </div>
        </div>
    </div>
    }
}

function RecommendedvideoPreview(props) {
    return <div class="video-item">
                <div class="thumbnail-container">
                    <VideoPreview 
                        video_length={props.video_length}
                        static_url={props.static_url}
                        animated_url={props.animated_url}
                        video_url={props.video_url}
                        channel={props.channel}
                    />
                </div>

                <div class="description">
                    <div class="title">{props.title}</div>
                    <div class="channel">{props.channel}</div>
                    <div class="views_date">{props.view_count} views • {props.upload_date}</div>
                </div>
            </div>;
}

function VideoComment(props) {
    return <div class="video-comment">
        <div class="comment-left">
            <img></img>
        </div>
        <div class="comment-right">
            <div class="comment-username">
                {props.username}
                {props.post_time}
            </div>
            <div class="comment-content">
                {props.content}
            </div>
        </div>
    </div>
}

export default Watch;

