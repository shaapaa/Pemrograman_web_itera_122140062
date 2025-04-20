import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

function BookForm({ onSubmit, selectedBook }) {
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [status, setStatus] = useState('miliki');

  useEffect(() => {
    if (selectedBook) {
      setTitle(selectedBook.title);
      setAuthor(selectedBook.author);
      setStatus(selectedBook.status);
    }
  }, [selectedBook]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title.trim() || !author.trim()) return alert("Form tidak boleh kosong!");
    const book = {
      id: selectedBook?.id || Date.now(),
      title,
      author,
      status
    };
    onSubmit(book);
    setTitle('');
    setAuthor('');
    setStatus('miliki');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input placeholder="Judul Buku" value={title} onChange={(e) => setTitle(e.target.value)} />
      <input placeholder="Penulis" value={author} onChange={(e) => setAuthor(e.target.value)} />
      <select value={status} onChange={(e) => setStatus(e.target.value)}>
        <option value="miliki">Dimiliki</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="beli">Ingin Dibeli</option>
      </select>
      <button type="submit">{selectedBook ? "Update" : "Tambah"}</button>
    </form>
  );
}

BookForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
  selectedBook: PropTypes.object
};

export default BookForm;
