import React, { Component, useEffect } from "react";
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import { useForm } from "react-hook-form";

import './loginwindow.scss'


function LoginWindow(props) {

    const { register, handleSubmit, watch, errors } = useForm();
    const onSubmit = (data) => {
        console.log(data);

        let formData = new FormData();
        formData.append('username', data['username']);
        formData.append('password', data['password'])
        formData.append('remember_me', 'false')

        fetch("/login?" + new URLSearchParams({
            username: data['username'],
            password: data['password'],
            remember_me: 'false'
        }), {
            method: 'post'
        })
        .then(response => response.json())
        .then(data => {
            if (data["result"] == "login_success") {
                window.location.reload();
            }
        })
    }



    return <div class="modal-content" id="modal-content">
    <div class="modal-header">
        <img src="https://youtube-clone-dev-storage.s3.us-east-2.amazonaws.com/web/icon.png"/>
        <p>Join Beamr today</p>
    </div>
    <Tabs>
        <TabList>
            <Tab>Log In</Tab>
            <Tab>Sign Up</Tab>
        </TabList>
    
        <TabPanel>
        <form onSubmit={handleSubmit(onSubmit)}>
            <div class="login-field">
                <p>Username</p>
                <input type="text" name="username" ref={register({required: true})}></input>
            </div>
            <div class="login-field">
                <p>Password</p>
                <input type="text" name="password" ref={register({required: true})}></input>
                {errors.exampleRequired && <span>This field is required</span>}
            </div>

            <button type="submit" class="login-button">Log in</button>
        </form>
        </TabPanel>
        <TabPanel>
            <div class="login-field">
                <p>Username</p>
                <input type="text"></input>
            </div>
            <div class="login-field">
                <p>Password</p>
                <input type="text"></input>
            </div>

            <div class="login-field">
                <p>Confirm Password</p>
                <input type="text"></input>
            </div>

            <div class="login-field">
                <p>Email</p>
                <input type="text"></input>
            </div>

            <button type="submit" class="login-button">Sign Up</button>
        </TabPanel>
    </Tabs>
    
</div>
        
}

export default LoginWindow;
