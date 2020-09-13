import React, { Component } from "react";
import './home.scss'
import VideoPreview from './VideoPreview'
import InfiniteScroll from 'react-infinite-scroll-component';

class Home extends Component {

    constructor(props) {
        super(props);
        this.state = {
            items: [],
            page_index: 12
        }

        fetch("/home_videos?start=0&num=12", {
        })
        .then(response => response.json())
        .then(data => {
            this.setState({
                items: this.state.items.concat(data["videos"])
            })
        })
        
    }

    fetchMoreData = () => {
        // a fake async api call like which sends
        // 20 more records in 1.5 secs
        fetch("/home_videos?start=" + this.state.page_index + "&num=12", {
        })
        .then(response => response.json())
        .then(data => {
            this.setState({
                items: this.state.items.concat(data["videos"]),
                page_index: this.state.page_index + 12
            })
        })
      };

    render() {
        return <div class="videos-container" id="videos-container">
            <InfiniteScroll
                dataLength={this.state.items.length}
                next={this.fetchMoreData}
                hasMore={true}
                scrollableTarget="videos-container"
                loader={<h4>Loading...</h4>}>
                    {this.state.items.map((val) => (
                        <VideoItem 
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
    }
}

function VideoItem(props) {
    return <div class="video-item">
                <div class="thumbnail-container">
                    <VideoPreview
                        static_url={props.static_url}
                        animated_url={props.animated_url}
                        video_length={props.video_length}
                        video_url={props.video_url}
                    />
                </div>

                <div class="description">
                    <div class="description-left">
                        <img src={props.profile_image_url}/>
                    </div>
                    <div class="description-right">
                        <div class="title">{props.title}</div>
                        <div class="channel">{props.channel}</div>
                        <div class="views_date">{props.view_count} views • {props.upload_date}</div>
                    </div>
                </div>
            </div>;
}

export default Home;
