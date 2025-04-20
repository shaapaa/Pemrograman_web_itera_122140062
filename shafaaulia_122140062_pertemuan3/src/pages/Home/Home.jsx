// src/pages/Home/Home.jsx
import React, { useState } from 'react';
import BookForm from '../../components/BookForm/BookForm';
import BookFilter from '../../components/BookFilter/BookFilter';
import SearchBar from '../../components/SearchBar/SearchBar';
import BookList from '../../components/BookList/BookList';
import { useBooks } from '../../context/BookContext';
import useFilterAndSearch from '../../hooks/useFilterAndSearch';
import './Home.css';

function Home() {
  const { books } = useBooks();
  const [filter, setFilter] = useState('all');
  const [search, setSearch] = useState('');
  const [editBook, setEditBook] = useState(null);

  const displayed = useFilterAndSearch(books, filter, search);

  return (
    <>
      <header className="site-header">
        <h1>Shafa's Mini Library</h1>
        <h4>Here's some books I have</h4>
      </header>

      <div className="container">
        <BookForm editBook={editBook} onComplete={() => setEditBook(null)} />
        <div className="filter-search">
          <BookFilter filter={filter} onFilterChange={setFilter} />
          <SearchBar search={search} onSearchChange={setSearch} />
        </div>
        <BookList books={displayed} onEdit={setEditBook} />
      </div>
      <footer className="site-footer">
            <h8>Shafa Aulia_122140062</h8>
      </footer>
    </>
  );
}

export default Home;
