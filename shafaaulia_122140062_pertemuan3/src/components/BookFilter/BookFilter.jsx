import React from 'react';
import PropTypes from 'prop-types';
import './BookFilter.css';

function BookFilter({ filter, onFilterChange }) {
  return (
    <div className="book-filter">
      <label>Status: </label>
      <select value={filter} onChange={e => onFilterChange(e.target.value)}>
        <option value="all">Semua</option>
        <option value="Punya sendiri">Punya sendiri</option>
        <option value="Sedang dibaca">Sedang dibaca</option>
        <option value="beli">Beli</option>
      </select>
    </div>
  );
}

BookFilter.propTypes = { filter: PropTypes.string.isRequired, onFilterChange: PropTypes.func.isRequired };

export default BookFilter;