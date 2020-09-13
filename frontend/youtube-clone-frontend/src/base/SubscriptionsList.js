import React, { Component } from "react";
import { FormProvider } from "react-hook-form";
import { useSelector, useDispatch } from 'react-redux';
import { subscriptionAdded } from '../app/subscriptionsSlice'

const SubscriptionsList = () => {
    const subscriptions = useSelector(state => state.subscriptions);
    const dispatch = useDispatch()
  
    const renderedSubscriptions = subscriptions.map(item => (
      <article className="post-excerpt" key={item.id}>
        <h3>{item.name}</h3>
      </article>
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
        <button onClick={newPost}>New Subscribe</button>
        <h2>Subscriptions</h2>
        {renderedSubscriptions}
      </section>
    )
  }

export default SubscriptionsList;
