import React from 'react'

const BookItem = ({book}) => {
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
        </tr>
    )
}

const BookList = ({books}) => {
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
            {books.map((book_) => <BookItem book={book_} />)}
        </table>
    )
}

export default BookList