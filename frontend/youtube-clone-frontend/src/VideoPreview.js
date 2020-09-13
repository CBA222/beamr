import React, { Component } from "react";
import { 
    Link
   } from "react-router-dom";
import './videopreview.scss'

class VideoPreview extends Component {
    constructor(props) {
        super(props);
        this.state = {
            classnames: 'animated'
        }

        this.mouseOver = this.mouseOver.bind(this);
        this.mouseOut = this.mouseOut.bind(this);
    }

    componentDidMount() {
        this.setState({
            classnames: 'animated'
        })
    }

    mouseOver() {
        this.setState({
            classnames: 'animated shown'
        })
    }

    mouseOut() {
        this.setState({
            classnames: 'animated'
        })
    }

    render() {
        return <div class="video-preview" onMouseEnter={this.mouseOver} onMouseLeave={this.mouseOut}>
            <div class="inside">
                <div class="inside-2">
                    <Link to={this.props.video_url}>
                    <div class="inside-3">
                        <img class="static" src={this.props.static_url}></img>
                        <img class={this.state.classnames} src={this.props.animated_url}></img>
                        <div class="video-length-container">
                            <span>{this.props.video_length}</span>
                        </div>
                    </div>
                    </Link>
                </div>
            </div>
        </div>
    }
    

}

export default VideoPreview;