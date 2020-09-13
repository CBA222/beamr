import { configureStore } from '@reduxjs/toolkit'

import userReducer from './userSlice'
import subscriptionsReducer from './subscriptionsSlice'

export default configureStore({
  reducer: {
    posts: userReducer,
    subscriptions: subscriptionsReducer
  }
})