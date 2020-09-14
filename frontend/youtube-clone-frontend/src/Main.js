import React, { Component } from "react";
import './base.scss'
import { 
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useLocation
 } from "react-router-dom";
import Modal from 'react-modal';
import Home from './Home'
import Watch from './Watch'
import VideoPreview from "./VideoPreview";
import LoginWindow from "./LoginWindow";
import Studio from "./studio/Studio";
import AccountModal from "./base/AccountModal"
import Results from "./Results";
import SubscriptionsList from './base/SubscriptionsList'
import SearchBar from './base/SearchBar'

function useQuery() {
  return new URLSearchParams(useLocation().search);
}

export function IO() {
  try {
    document.getElementById("signup-button").addEventListener("click", function(){ 
      let sidebar_full = document.getElementById("sidebar-full");
      sidebar_full.classList.toggle("expanded");
      sidebar_full.classList.toggle("collapsed");
  
      let sidebar_mini = document.getElementById("sidebar-mini");
      sidebar_mini.classList.toggle("expanded");
      sidebar_mini.classList.toggle("collapsed");
  
      let content_container = document.getElementById("content-container");
      content_container.classList.toggle("expanded");
      content_container.classList.toggle("collapsed");
    });
  } catch(err) {

  }
  
}
 
class Main extends Component {

  constructor(props) {
    super(props);
    this.state = {
      loggedIn: false,
      openLogin: false,
      openAccount: false,
      loginModalStyles: {
        content : {
          position: "fixed",
          top: "50%",
          right: "auto",
          bottom: "auto",
          left: "50%",
          transform: "translate(-50%,-50%)",
          outline: "0",
          padding: "0",
          border: "0",
          "border-radius": "0"
        },
        overlay: {
          "background-color": "rgba(0, 0, 0, 0.6)"
        }
      }
    }

    this.sidebarFull = React.createRef();
    this.sidebarMini = React.createRef();
    this.contentContainer = React.createRef();
    this.loginModal = React.createRef();
    this.accountModal = React.createRef();
    this.loginButton = React.createRef();
    this.signupButton = React.createRef();
    this.accountButton = React.createRef();

    this.sidebarOpen = this.sidebarOpen.bind(this);
    this.sidebarClose = this.sidebarClose.bind(this);
    this.openAccountModal = this.openAccountModal.bind(this);
    this.closeAccountModal = this.closeAccountModal.bind(this);
    this.openLoginModal = this.openLoginModal.bind(this);
    this.closeLoginModal = this.closeLoginModal.bind(this);


    fetch("/profile", {
    })
    .then(response => response.json())
    .then(data => {
        this.setState({
            loggedIn: data["logged_in"]
        })
        if (data["logged_in"]) {
          //this.updateIOAccount();
        } else {
          //this.updateIOLogin();
        }
    })
  }

  componentDidMount() {
    
  }

  openAccountModal() {
    this.setState({
      openAccount: true
    });
  }

  closeAccountModal() {
    this.setState({
      openAccount: false
    });
  }

  openLoginModal() {
    this.setState({
      openLogin: true
    });
  }

  closeLoginModal() {
    this.setState({
      openLogin: false
    });
  }

  sidebarOpen() {
    this.sidebarFull.current.classList.toggle("expanded");
    this.sidebarFull.current.classList.toggle("collapsed");
    this.sidebarMini.current.classList.toggle("expanded");
    this.sidebarMini.current.classList.toggle("collapsed");
    this.contentContainer.current.classList.toggle("expanded");
    this.contentContainer.current.classList.toggle("collapsed");
  }

  sidebarClose() {
    this.sidebarFull.current.classList.toggle("expanded");
    this.sidebarFull.current.classList.toggle("collapsed");
    this.sidebarMini.current.classList.toggle("expanded");
    this.sidebarMini.current.classList.toggle("collapsed");
    this.contentContainer.current.classList.toggle("expanded");
    this.contentContainer.current.classList.toggle("collapsed");
  }

  searchSubmit() {

  }

  render() {
    const loggedIn = this.state.loggedIn;
  return (
    <Router>
      <div id="main">
        <Modal
            isOpen={this.state.openLogin}
            onRequestClose={this.closeLoginModal}
            style={this.state.loginModalStyles}
          >
            <LoginWindow ref={this.loginModal} open={this.state.openLogin} close={this.closeLoginModal}/>
          </Modal>

        <Modal
            isOpen={this.state.openAccount}
            onRequestClose={this.closeAccountModal}
            style={this.state.loginModalStyles}
          >
            <AccountModal ref={this.accountModal}/>
        </Modal>
        
        
        <div class="header" id="main-header">
          <div class="header-left">
              <Link to="/"><img class="website-icon" src="https://youtube-clone-dev-storage.s3.us-east-2.amazonaws.com/web/icon.png"/></Link>
              <ul class="nav">
                  <li><Link to="/">Trending</Link></li>
                  <li><Link to="/watch?id=98">Music</Link></li>
                  <li><Link to="/search?q=react">Games</Link></li>
              </ul>
          </div>
          <div class="header-center">
              <SearchBar/>
          </div>
          
          {loggedIn  
            ? <div class="header-right">
                <div class="account-button" id="account-button" onClick={this.openAccountModal}>
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
              </div>
            : <div class="header-right">
                <button class="ui-button login-button" onClick={this.openLoginModal}>Log In</button>
                <button class="ui-button signup-button" onClick={this.openLoginModal}>Sign Up</button>
                
              </div>
          }
        </div>
      <div class="sidebar-full collapsed" id="sidebar-full" ref={this.sidebarFull}>
        <div class="header">
          <button onClick={this.sidebarClose}>Close</button>
            <p>SUBSCRIPTIONS</p>
        </div>
        <div class="subscribed-list">
            <ul>
                <li>
                    <div class="subscribed-item">
                        <div class="subscribed-item-left">
                            <img class="subscribed-icon" src=""/>
                        </div>
                        <div class="subscribed-item-right">
                            <p class="channel-name">Channel Name</p>
                            <p class="subscriber-count">9.8m subscribers</p>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
      </div>
      <div class="sidebar-mini expanded" id="sidebar-mini" ref={this.sidebarMini}>
        <button onClick={this.sidebarOpen}>Open</button>
      </div>
      <div class="content-container collapsed" id="content-container" ref={this.contentContainer}>
        <Switch>
          <Route exact path="/" component={Home}/>
          <Route path="/watch" component={Watch}/>
          <Route path="/search" component={Results}/>
          <Route path='/studio' component={Studio}/>
        </Switch>
      </div>
    </div>
    </Router>
  )
  }
}
 
export default Main;