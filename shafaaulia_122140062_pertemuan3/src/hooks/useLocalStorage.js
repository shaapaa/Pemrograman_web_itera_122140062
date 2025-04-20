// Custom Hook `useLocalStorage`
// Mengelola penyimpanan state di localStorage dengan Hooks

import { useState, useEffect } from 'react';

function useLocalStorage(key, initialValue) {
  // Ambil dari localStorage atau gunakan initialValue
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error('useLocalStorage getItem error:', error);
      return initialValue;
    }
  });

  // Sync ke localStorage setiap perubahan
  useEffect(() => {
    try {
      window.localStorage.setItem(key, JSON.stringify(storedValue));
    } catch (error) {
      console.error('useLocalStorage setItem error:', error);
    }
  }, [key, storedValue]);

  return [storedValue, setStoredValue];
}

export default useLocalStorage;
