import React from 'react';
import useBookStats from '../../hooks/useBookStats';
import './Stats.css';

export default function Stats() {
  const { total, miliki, baca, beli } = useBookStats();
  return (
    <div className="stats-page">
      <h2>Statistik Buku</h2>
      <ul>
        <li>Total Buku        : {total}</li>
        <li>Dimiliki          : {miliki}</li>
        <li>Sedang Dibaca     : {baca}</li>
        <li>Ingin Dibeli      : {beli}</li>
      </ul>
    </div>
  );
}
