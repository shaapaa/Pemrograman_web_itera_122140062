// BookForm.jsx
// Form input untuk menambahkan atau mengedit buku
// Menggunakan useState untuk form state (judul, penulis, status)
// Validasi form disertai error handling
// Dispatch ke context dengan action ADD_BOOK atau UPDATE_BOOK

import React, { useState, useEffect } from 'react';
import { useBooks } from '../../context/BookContext';
import PropTypes from 'prop-types';
import './BookForm.css';

function BookForm({ editBook, onComplete }) {
  const { dispatch } = useBooks();
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [status, setStatus] = useState('Status');
  const [errors, setErrors] = useState({});

  useEffect(() => {
    if (editBook) {
      setTitle(editBook.title);
      setAuthor(editBook.author);
      setStatus(editBook.status);
    }
  }, [editBook]);

  const validate = () => {
    const errs = {};
    if (!title.trim()) errs.title = 'Judul wajib diisi.';
    if (!author.trim()) errs.author = 'Penulis wajib diisi.';
    if (!status) errs.status = 'Status wajib dipilih.';
    setErrors(errs);
    return Object.keys(errs).length === 0;
  };

  const handleSubmit = e => {
    e.preventDefault();
    if (!validate()) return;

    const payload = { id: editBook?.id || Date.now(), title, author, status };
    dispatch({ type: editBook ? 'UPDATE_BOOK' : 'ADD_BOOK', payload });
    setTitle(''); setAuthor(''); setStatus('Status'); setErrors({});
    if (onComplete) onComplete();
  };

  return (
    <form className="book-form" onSubmit={handleSubmit}>
      <div>
        <input value={title} onChange={e => setTitle(e.target.value)} placeholder="Judul Buku" />
        {errors.title && <small className="error">{errors.title}</small>}
      </div>
      <div>
        <input value={author} onChange={e => setAuthor(e.target.value)} placeholder="Penulis" />
        {errors.author && <small className="error">{errors.author}</small>}
      </div>
      <div>
        <select value={status} onChange={e => setStatus(e.target.value)}>
          <option value="Punya sendiri">Punya sendiri</option>
          <option value="Sedang dibaca">Sedang dibaca</option>
          <option value="beli">Beli</option>
        </select>
        {errors.status && <small className="error">{errors.status}</small>}
      </div>
      <button type="submit">{editBook ? 'Update' : 'Tambah'} Buku</button>
      {editBook && <button type="button" onClick={onComplete}>Batal</button>}
    </form>
  );
}

BookForm.propTypes = {
  editBook: PropTypes.shape({ id: PropTypes.number, title: PropTypes.string, author: PropTypes.string, status: PropTypes.string }),
  onComplete: PropTypes.func,
};

BookForm.defaultProps = { editBook: null, onComplete: null };

export default BookForm;
