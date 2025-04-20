// BookList.jsx
// Menampilkan daftar buku dalam bentuk card layout
// Menerima prop `onEdit` untuk mengisi form edit di BookForm

import React from 'react';
import PropTypes from 'prop-types';
import { useBooks } from '../../context/BookContext';
import './BookList.css';

function BookList({ books, onEdit }) {
  const { dispatch } = useBooks();
  const handleDelete = id => dispatch({ type: 'DELETE_BOOK', payload: id });

  if (!books.length) return <p className="no-books">Tidak ada buku.</p>;

  return (
    <ul className="book-list">
      {books.map(book => (
        <li key={book.id} className="book-item">
          <div className="book-info">
            <strong>{book.title}</strong> oleh {book.author} <em>({book.status})</em>
          </div>
          <div className="book-actions">
            <button onClick={() => onEdit(book)}>Edit</button>
            <button onClick={() => handleDelete(book.id)}>Hapus</button>
          </div>
        </li>
      ))}
    </ul>
  );
}

BookList.propTypes = {
  books: PropTypes.array.isRequired,
  onEdit: PropTypes.func.isRequired,
};

export default BookList;
