import React, { Component } from "react";
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import { useForm } from "react-hook-form";
import UploadModal from './UploadModal'

import './studio.scss'


class Studio extends Component {

    constructor(props) {
        super(props);
        this.state = {
            'username': "none"
        }
    }

    componentDidMount() {
        document.title = "Creator dashboard"
        fetch("/profile", {
        })
        .then(response => response.json())
        .then(data => {
            this.setState({
                username: data['username']
            })
        })
        this.updateIO();
    }

    updateIO() {
        var modal = document.getElementById("upload-modal");
        var modal_button = document.getElementById("upload-button");
    
        modal_button.addEventListener('click', function() {
            modal.style.display="flex";
        })
      }


    render() {
        return <div class="studio">
            <UploadModal/>
            <div class="studio-header">
                <div class="studio-title">
                    Channel Videos
                </div>
                <button class="upload-button" id="upload-button">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                        <path fillRule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM6.293 6.707a1 1 0 010-1.414l3-3a1 1 0 011.414 0l3 3a1 1 0 01-1.414 1.414L11 5.414V13a1 1 0 11-2 0V5.414L7.707 6.707a1 1 0 01-1.414 0z" clipRule="evenodd" />
                    </svg>
                    <p>UPLOAD</p>
                </button>
            </div>
            <div class="uploaded-videos-container">
                <table>
                    <thead>
                        <tr>
                            <th>Video</th>
                            <th>Date</th>
                            <th>Views</th>
                            <th>Comments</th>
                            <th>Likes (vs dislikes)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th></th>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    }
}

export default Studio;
