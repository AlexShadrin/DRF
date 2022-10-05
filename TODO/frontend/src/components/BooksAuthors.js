import React from "react";
import {useParams} from "react-router-dom";

const BookItem =({book}) => {
    return(
        <tr>
            <td>{book.id}</td>
            <td>{book.name}</td>
            <td>{book.authors}</td>
        </tr>
    )
}

const BooksAuthors= ({books}) => {
    let {authorId} = useParams()
    console.log(authorId)
    let  filter_books = books.filter((book) => book.authors.includes(parseInt(authorId)))
    return(
        <table>
            <th>ID</th>
            <th>Name</th>
            <th>Authors</th>
            {filter_books.map((book_) => <BookItem book={book_}/>)}
        </table>
    )
}

export default BooksAuthors