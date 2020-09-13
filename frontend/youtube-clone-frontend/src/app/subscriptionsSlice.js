import { createSlice } from '@reduxjs/toolkit'

const initialState = [
  { id: '1', name: 'TaylorSwiftVEVO', url: 'Hello!', icon_url: '', subscriber_count: '' },
  { id: '2', name: 'EminemVEVO', url: 'More text', icon_url: '', subscriber_count: '' }
]

const subscriptionsSlice = createSlice({
  name: 'subscriptions',
  initialState,
  reducers: {
    subscriptionAdded(state, action) {
      state.push(action.payload)
    }
  }
})

export const { subscriptionAdded } = subscriptionsSlice.actions

export default subscriptionsSlice.reducer