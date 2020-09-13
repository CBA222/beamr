import React, { Component } from "react";
import { useForm } from "react-hook-form";

import './uploadmodal.scss'


class UploadModal extends Component {

    constructor(props) {
        super(props);
    }

    componentDidMount() {
    }

    closeWindow() {
        document.getElementById("upload-modal").style.display = 'none'
    }


    render() {
        return <div class="upload-modal" id="upload-modal">
            <div class="modal-content">
                <div class="upload-header">
                    <p>Upload Video</p>
                    <button onClick={this.closeWindow} class="close-button">X</button>
                </div>
                <div class="main-content">
                    <div class="upload-video-zone">
                        <div class="upload-text">
                            Drag and drop video files to upload
                        </div>
                        <input type="file"></input>
                    </div>
                </div>
            </div>
            
        </div>
    }
}

export default UploadModal;
