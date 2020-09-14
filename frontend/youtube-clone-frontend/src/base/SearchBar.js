import React, { Component, useEffect, useState, useCallback } from "react";
import { FormProvider } from "react-hook-form";
import { useHistory } from "react-router-dom";

import './SearchBar.scss'

const SearchBar = (props) => {

    const [value, setValue] = useState("");
    let history = useHistory();

    const handleSubmit = useCallback((event) => {
        event.preventDefault();
        history.push('/search?q=' + value);
    })

    const handleChange = useCallback((event) => {
        setValue(event.target.value);
    })

    return(
        <div class="searchbar-container">
            <form>
            <div class="query-box">
                <input autocomplete="off" type="text" id="query" placeholder="Search" value={value} onChange={handleChange} required/>
            </div>
            <div class="search-button-box">
                <button type="submit" onClick={handleSubmit}>
                </button>
            </div>
            </form>
        </div>
    )
}

export default SearchBar;