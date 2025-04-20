// test BookForm component
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import BookForm from '../components/BookForm/BookForm';
import { BookProvider } from '../context/BookContext';

describe('BookForm', () => {
  test('renders input fields and button', () => {
    render(
      <BookProvider>
        <BookForm />
      </BookProvider>
    );
    expect(screen.getByPlaceholderText(/Judul Buku/i)).toBeInTheDocument();
    expect(screen.getByPlaceholderText(/Penulis/i)).toBeInTheDocument();
    expect(screen.getByRole('combobox')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Tambah Buku/i })).toBeInTheDocument();
  });

  test('shows validation errors when submitting empty form', () => {
    render(
      <BookProvider>
        <BookForm />
      </BookProvider>
    );
    fireEvent.click(screen.getByRole('button', { name: /Tambah Buku/i }));
    expect(screen.getByText(/Judul wajib diisi\./i)).toBeInTheDocument();
    expect(screen.getByText(/Penulis wajib diisi\./i)).toBeInTheDocument();
  });
});