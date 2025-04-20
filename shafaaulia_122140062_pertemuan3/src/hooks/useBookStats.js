// Menghitung jumlah buku per status untuk halaman statistik
import { useMemo } from 'react';
import PropTypes from 'prop-types';

function useBookStats(books) {
  return useMemo(() => {
    const stats = { Punyasendiri: 0, baca: 0, beli: 0 };
    books.forEach(book => {
      if (stats[book.status] !== undefined) stats[book.status]++;
    });
    return {
      total: books.length,
      ...stats
    };
  }, [books]);
}

useBookStats.propTypes = {
  books: PropTypes.arrayOf(
    PropTypes.shape({
      status: PropTypes.oneOf(['Punya sendiri','baca','beli']).isRequired,
    })
  )
};

export default useBookStats;
