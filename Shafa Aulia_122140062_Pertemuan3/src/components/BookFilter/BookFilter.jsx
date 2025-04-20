import React from 'react';
import PropTypes from 'prop-types';

/**
 * BookFilter
 * Menyajikan UI untuk:
 *  - Memilih status buku (Dimiliki / Sedang Dibaca / Ingin Dibeli)
 *  - Mengetik kata kunci untuk pencarian judul atau penulis
 */
function BookFilter({ filterStatus, onFilterChange, searchTerm, onSearchChange }) {
  return (
    <div className="book-filter">
      {/* Dropdown untuk filter status */}
      <select
        value={filterStatus}
        onChange={e => onFilterChange(e.target.value)}
      >
        <option value="">Semua Status</option>
        <option value="miliki">Dimiliki</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="beli">Ingin Dibeli</option>
      </select>

      {/* Input untuk pencarian */}
      <input
        type="text"
        placeholder="Cari judul atau penulis..."
        value={searchTerm}
        onChange={e => onSearchChange(e.target.value)}
      />
    </div>
  );
}

BookFilter.propTypes = {
  filterStatus:  PropTypes.string.isRequired,
  onFilterChange: PropTypes.func.isRequired,
  searchTerm:    PropTypes.string.isRequired,
  onSearchChange: PropTypes.func.isRequired
};

export default BookFilter;
