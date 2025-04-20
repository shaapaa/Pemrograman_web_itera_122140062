import React from 'react';
import PropTypes from 'prop-types';
import './BookCardList.css';

function BookCardList({ books }) {
  if (!books.length) return <p className="no-books">Tidak ada buku.</p>;

  return (
    <div className="book-card-grid">
      {books.map(book => (
        <div key={book.id} className="book-card">
          <h3>{book.title}</h3>
          <p><strong>Penulis:</strong> {book.author}</p>
          <p><strong>Status:</strong> {book.status}</p>
        </div>
      ))}
    </div>
  );
}

BookCardList.propTypes = {
  books: PropTypes.array.isRequired,
};

export default BookCardList;
