import { useMemo } from 'react';
import { useBooks } from '../context/BookContext';

/**
 * useBookStats
 * Menghitung statistik jumlah buku per status dan total.
 */
export default function useBookStats() {
  const { books } = useBooks();
  return useMemo(() => {
    const total = books.length;
    const miliki = books.filter(b => b.status === 'miliki').length;
    const baca   = books.filter(b => b.status === 'baca').length;
    const beli   = books.filter(b => b.status === 'beli').length;
    return { total, miliki, baca, beli };
  }, [books]);
}
