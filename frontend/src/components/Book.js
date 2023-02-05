import React from 'react'

const BookItem = ({book,delete_book}) => {
    return (
        <tr>
            <td>
                {book.id}
            </td>
            <td>
                {book.name}
            </td>
            <td>
                {book.authors}
            </td>
            <td>
               <button onClick={()=>delete_book(book.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const BookList = ({books,delete_book}) => {
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                Name
            </th>
            <th>
                Authors
            </th>
            <th>
            </th>
            {books.map((book) => <BookItem book={book} delete_book={delete_book}/>)}
        </table>
    )
}

export default BookList