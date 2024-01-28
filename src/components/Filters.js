import React from "react";
import Checkbox from "./Checkbox"
import "../index.css"

function Filters(props){

    if (props.text === "Size"){
        return(
            <div class="box">
            <h2>{props.text}</h2>
                <form action="#">
                    <Checkbox text="Montreal Only"/>
                    <Checkbox text="Quebec Chain"/>
                    <Checkbox text="National Chain"/>
                    <Checkbox text="International Chain"/>
                </form>
            </div>
        );
    }
    else if (props.text === "Warning"){
        return(
            <div class="box">
            <h2>{props.text}</h2>
                <form action="#">
                    <Checkbox text = "Without Past Health Warnings"/>
                </form>
            </div>
        );
    }
    else if (props.text === "Price"){
        return(
            <div class="box">
            <h2>{props.text}</h2>
                <form action="#">
                    <Checkbox text="$"/>
                    <Checkbox text="$$"/>
                    <Checkbox text="$$$"/>
                    <Checkbox text="$$$$"/>
                </form>
            </div>
        );
    }
    else if (props.text === "Location"){
        return(
            <div class="box">
            <h2>{props.text}</h2>
                <form action="#">
                    <Checkbox text="Plateau"/>
                    <Checkbox text="Cote-Des-Neiges"/>
                    <Checkbox text="Chinatown"/>
                    <Checkbox text="Little Italy"/>
                    <Checkbox text="Old Montreal"/>
                    <Checkbox text="Mile End"/>
                    <Checkbox text="Quartier Latin"/>
                </form>
            </div>
        );
    }
}

export default Filters;
