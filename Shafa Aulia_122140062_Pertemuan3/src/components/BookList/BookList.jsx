import React from 'react';
import PropTypes from 'prop-types';

/**
 * BookList
 * Menerima daftar buku (setelah difilter & dicari), lalu:
 *  - Menampilkan setiap buku
 *  - Tombol Edit memanggil onEdit(book)
 *  - Tombol Hapus memanggil onDelete(book.id)
 */
function BookList({ books, onEdit, onDelete }) {
  if (books.length === 0) {
    return <p className="empty-message">Tidak ada buku untuk ditampilkan.</p>;
  }

  return (
    <ul className="book-list">
      {books.map(book => (
        <li key={book.id} className="book-item">
          <div className="book-info">
            <h3>{book.title}</h3>
            <p>Penulis: {book.author}</p>
            <p>Status: { 
              book.status === 'miliki' ? 'Dimiliki' :
              book.status === 'baca'   ? 'Sedang Dibaca' :
              'Ingin Dibeli'
            }</p>
          </div>
          <div className="book-actions">
            <button onClick={() => onEdit(book)}>Edit</button>
            <button onClick={() => onDelete(book.id)}>Hapus</button>
          </div>
        </li>
      ))}
    </ul>
  );
}

BookList.propTypes = {
  books:    PropTypes.arrayOf(PropTypes.shape({
    id:     PropTypes.number.isRequired,
    title:  PropTypes.string.isRequired,
    author: PropTypes.string.isRequired,
    status: PropTypes.oneOf(['miliki','baca','beli']).isRequired
  })).isRequired,
  onEdit:   PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired
};

export default BookList;
