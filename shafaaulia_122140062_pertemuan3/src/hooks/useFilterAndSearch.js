import { useMemo } from 'react';

/**
 * Mengembalikan daftar buku yang sudah difilter dan dicari.
 *
 * @param {Array} books
 * @param {string} filter - 'all' | 'Punya sendiri' | 'baca' | 'beli'
 * @param {string} search
 */
export default function useFilterAndSearch(books, filter, search) {
  return useMemo(() => {
    const term = search.trim().toLowerCase();
    return books.filter(book => {
      const matchesStatus = filter === 'all' || book.status === filter;
      const matchesSearch =
        !term ||
        book.title.toLowerCase().includes(term) ||
        book.author.toLowerCase().includes(term);
      return matchesStatus && matchesSearch;
    });
  }, [books, filter, search]);
}
