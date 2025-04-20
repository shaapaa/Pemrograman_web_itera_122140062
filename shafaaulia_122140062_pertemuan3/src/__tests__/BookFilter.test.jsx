// test BookFilter component
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import BookFilter from '../components/BookFilter/BookFilter';

describe('BookFilter', () => {
  test('memanggil onFilterChange saat opsi dipilih', () => {
    const onFilterChange = jest.fn();
    render(<BookFilter filter="all" onFilterChange={onFilterChange} />);
    fireEvent.change(screen.getByRole('combobox'), { target: { value: 'baca' } });
    expect(onFilterChange).toHaveBeenCalledWith('baca');
  });
});
