// test BookContext component
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { BookProvider, useBooks } from '../context/BookContext';

function TestComponent() {
  const { books, dispatch } = useBooks();
  return (
    <div>
      <span data-testid="count">{books.length}</span>
      <button onClick={() => dispatch({ type: 'ADD_BOOK', payload: { id: 3, title: 'Test', author: 'A', status: 'milik' } })}>
        Add
      </button>
    </div>
  );
}

describe('BookContext', () => {
  test('adds a book to context', () => {
    render(
      <BookProvider>
        <TestComponent />
      </BookProvider>
    );
    const count = screen.getByTestId('count');
    expect(count.textContent).toBe('0');
    fireEvent.click(screen.getByRole('button', { name: /Add/i }));
    expect(count.textContent).toBe('1');
  });
});
