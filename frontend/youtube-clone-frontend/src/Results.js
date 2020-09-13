import React, { Component } from "react";
import { FormProvider } from "react-hook-form";
import { useSelector, useDispatch } from 'react-redux';
import { subscriptionAdded } from './app/subscriptionsSlice'

const Results = () => {
    const subscriptions = useSelector(state => state.subscriptions);
    const dispatch = useDispatch()
  
    const renderedPosts = subscriptions.map(item => (
      <div className="subscription-item" key={item.id}>
        <div class="item-left">
          <img src={item.icon_url}></img>
        </div>
        <div class="item-right">
          <div class="item-name">{item.name}</div>
          <div class="item-sub-count">{item.subscriber_count}</div>
        </div>
      </div>
    ))


    const newPost = () => {
      dispatch(
        subscriptionAdded({
          id:99,
          name: "My username"
        })
      )
    }
  
    return (
      <section>
        <button onClick={newPost}>Submit new post</button>
        <h2>Posts</h2>
        {renderedPosts}
      </section>
    )
  }

export default Results;
