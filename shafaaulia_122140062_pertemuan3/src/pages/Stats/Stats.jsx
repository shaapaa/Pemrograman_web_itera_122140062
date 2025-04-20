import React from 'react';
import { useBooks } from '../../context/BookContext';
import BookCardList from '../../components/BookCardList/BookCardList';
import './Stats.css';

function Stats() {
  const { books } = useBooks();
  const total = books.length;
  const byStatus = books.reduce((acc, b) => ({ ...acc, [b.status]: (acc[b.status] || 0) + 1 }), {});

  return (
    <div className="stats">
      <h2>Statistik Buku</h2>
      <p>Total Buku: {total}</p>
      <BookCardList books={books} />
    </div>
  );
}

export default Stats;
