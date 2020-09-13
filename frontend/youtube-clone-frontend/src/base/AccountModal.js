import React, { Component } from "react";
import { 
    Link
} from "react-router-dom";

import './accountmodal.scss'


class AccountModal extends Component {

    constructor(props) {
        super(props);
        this.state = {
            username: "NONE"
        }
    }

    componentDidMount() {
        fetch("/profile", {
        })
        .then(response => response.json())
        .then(data => {
            this.setState({
                username: data['username']
            })
        })
    }

    logout() {
        fetch("/logout", {
            method: 'post'
        })
        .then(response => response.json())
        .then(data => {
            window.location.replace('/');
        })
    }


    render() {
        return <div class="account-modal" id="account-modal">
            <div class="modal-top">
                <img src=""></img>
                <p>{this.state.username}</p>
            </div>

            <div class="modal-bottom">
                <Link to="">
                    <div class="modal-button">
                        <img></img>
                        <p>Your Channel</p>
                    </div>
                </Link>
                <Link to="/studio">
                    <div class="modal-button">
                        <img></img>
                        <p>Creator Dashboard</p>
                    </div>
                </Link>
                <Link to="">
                    <div class="modal-button">
                        <img></img>
                        <p>Settings</p>
                    </div>
                </Link>
                <div class="modal-button" onClick={this.logout}>
                    <img></img>
                    <p>Log Out</p>
                </div>
                
            </div>
        </div>
    }
}

export default AccountModal;
