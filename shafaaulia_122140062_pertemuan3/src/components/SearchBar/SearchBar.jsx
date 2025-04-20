// Komponen reusable input pencarian berdasarkan judul atau penulis
import React from 'react';
import PropTypes from 'prop-types';
import './SearchBar.css';

function SearchBar({ search, onSearchChange }) {
  return (
    <div className="search-bar">
      <input value={search} onChange={e => onSearchChange(e.target.value)} placeholder="Cari judul atau penulis..." />
    </div>
  );
}

SearchBar.propTypes = { search: PropTypes.string.isRequired, onSearchChange: PropTypes.func.isRequired };

export default SearchBar;
