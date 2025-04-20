import React, { useState } from 'react';
import { useBooks } from '../../context/BookContext';
import BookForm from '../../components/BookForm/BookForm';
import BookFilter from '../../components/BookFilter/BookFilter';
import BookList from '../../components/BookList/BookList';
import './Home.css';

export default function Home() {
  const { books, dispatch } = useBooks();
  const [filterStatus, setFilterStatus] = useState('');
  const [searchTerm, setSearchTerm]     = useState('');
  const [selectedBook, setSelectedBook] = useState(null);

  // Filter + search
  const filtered = books
    .filter(b => !filterStatus || b.status === filterStatus)
    .filter(b =>
      b.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      b.author.toLowerCase().includes(searchTerm.toLowerCase())
    );

  // Handlers CRUD
  const handleSubmit = (book) => {
    if (selectedBook) {
      dispatch({ type: 'UPDATE_BOOK', payload: book });
    } else {
      dispatch({ type: 'ADD_BOOK', payload: book });
    }
    setSelectedBook(null);
  };
  const handleEdit   = (book) => setSelectedBook(book);
  const handleDelete = (id)   => dispatch({ type: 'DELETE_BOOK', payload: id });

  return (
    <div className="home">
      <h2>Daftar Buku Saya</h2>
      <BookForm onSubmit={handleSubmit} selectedBook={selectedBook} />
      <BookFilter
        filterStatus={filterStatus}
        onFilterChange={setFilterStatus}
        searchTerm={searchTerm}
        onSearchChange={setSearchTerm}
      />
      <BookList books={filtered} onEdit={handleEdit} onDelete={handleDelete} />
    </div>
  );
}
