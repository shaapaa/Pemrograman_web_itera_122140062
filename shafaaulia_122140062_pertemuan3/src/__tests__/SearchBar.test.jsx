// test search bar component
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import SearchBar from '../components/SearchBar/SearchBar';

describe('SearchBar', () => {
  test('memanggil onSearchChange saat input berubah', () => {
    const onSearchChange = jest.fn();
    render(<SearchBar search="" onSearchChange={onSearchChange} />);
    fireEvent.change(
      screen.getByPlaceholderText(/cari judul atau penulis/i),
      { target: { value: 'test' } }
    );
    expect(onSearchChange).toHaveBeenCalledWith('test');
  });
});
