import React, { Component } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

/*const list = [
    {
        "id":1,
        "title":"meto",
        "body":"tome"
    },
    {
        "id":2,
        "title":"ssss",
        "body":"ddddd"
    }
]

class App extends Component {
  constructor(props){
      super(props);
      this.state = { list };
  }
  
  render() {
    return (
      <div>
        {this.state.list.map(item => (
            <div key={item.id}>
            <h1>{item.title}</h1>
            <p>{item.body}</p>
            </div>
        ))}
      </div>
    );
  }
}*/
class App extends Component {
    state = {
        todos : []
    }
    
    componentDidMount() {
        this.getTodos();
    }
    
    getTodos() {
        axios
            .get('http://127.0.0.1:8000/api/')
            .then(res => {
                this.setState({ todos: res.data });
            })
            .catch(err => {
                console.log(err);
            });
    }
    render() {
    return (
      <div>
        {this.state.todos.map(item => (
            <div key={item.id}>
            <h1>{item.title}</h1>
            <p>{item.body}</p>
            </div>
        ))}
      </div>
    );
  }
}
    

export default App;














