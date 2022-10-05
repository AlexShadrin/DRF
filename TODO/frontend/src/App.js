import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import axios from 'axios';
import BookList from './components/Book.js';
import {BrowserRouter,Route,Routes,Link,Navigate} from "react-router-dom";
import NotFound404 from "./components/NotFound404";
import BooksAuthors from "./components/BooksAuthors";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': [],
        }
    }
    componentDidMount() {

        axios.get('http://127.0.0.1:8000/api/authors')
            .then(response => {
                const authors = response.data
                    this.setState(
                    {
                        'authors': authors
                    }
                )
            }).catch(error => console.log(error))

       axios.get('http://127.0.0.1:8000/api/books')
            .then(response => {
                const books = response.data
                    this.setState(
                    {
                        'books': books
                    }
                )
            }).catch(error => console.log(error))
    }

    render () {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li>
                            <Link to='/'>Authors</Link>
                        </li>
                        <li>
                            <Link to='/books'>Books</Link>
                        </li>
                    </nav>

                    <Routes>
                        <Route exact path='/' element={<Navigate to='/authors'/>}/>
                        <Route path='/authors'>
                            <Route index element={<AuthorList authors={this.state.authors}/>}/>
                            <Route path=':authorId' element={<BooksAuthors books={this.state.books}/>}/>
                        </Route>

                        <Route exact path ='/books' element={<BookList books={this.state.books}/>} />
                        <Route path='*' element={<NotFound404/>}/>
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;