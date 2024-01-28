
function Checkbox(props){
    return(
    <div>
        <input type="checkbox" id="option" name="option" />
        <label for="option">{props.text}</label>
    </div>
    )
}

export default Checkbox;