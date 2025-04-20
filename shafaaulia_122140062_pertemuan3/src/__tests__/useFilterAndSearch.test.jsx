// test useFilterAndSearch hook
import React from 'react';
import { render, screen } from '@testing-library/react';
import useFilterAndSearch from '../hooks/useFilterAndSearch';

function HookTester({ books, filter, search }) {
  const result = useFilterAndSearch(books, filter, search);
  return <div data-testid="len">{result.length}</div>;
}

describe('useFilterAndSearch hook', () => {
  const books = [
    { id: 1, title: 'React Guide', author: 'Dan', status: 'milik' },
    { id: 2, title: 'Vue for Beginners', author: 'Evan', status: 'baca' },
  ];

  test('returns all when filter=all & empty search', () => {
    render(<HookTester books={books} filter="all" search="" />);
    expect(screen.getByTestId('len').textContent).toBe('2');
  });

  test('filters by status & search term', () => {
    render(<HookTester books={books} filter="baca" search="Vue" />);
    expect(screen.getByTestId('len').textContent).toBe('1');
  });
});
