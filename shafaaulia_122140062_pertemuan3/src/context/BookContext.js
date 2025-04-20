// BookContext.jsx
// Mengelola state global untuk daftar buku menggunakan Context API dan Reducer
// Memungkinkan komponen mana pun untuk mengakses dan memodifikasi daftar buku tanpa prop drilling

import React, { createContext, useContext } from 'react';
import useLocalStorage from '../hooks/useLocalStorage';
import PropTypes from 'prop-types';

const BookContext = createContext();

const bookReducer = (state, action) => {
  switch (action.type) {
    case 'ADD_BOOK':
      return [...state, action.payload];
    case 'UPDATE_BOOK':
      return state.map(b => b.id === action.payload.id ? action.payload : b);
    case 'DELETE_BOOK':
      return state.filter(b => b.id !== action.payload);
    default:
      return state;
  }
};

export function BookProvider({ children }) {
  const [books, setBooks] = useLocalStorage('books', []);
  const dispatch = action => setBooks(bookReducer(books, action));

  return (
    <BookContext.Provider value={{ books, dispatch }}>
      {children}
    </BookContext.Provider>
  );
}

BookProvider.propTypes = {
  children: PropTypes.node.isRequired,
};

export function useBooks() {
  const context = useContext(BookContext);
  if (!context) throw new Error('useBooks must be used within BookProvider');
  return context;
}
