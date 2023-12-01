
export const isAuthenticated = () => {
    const storedUsername = localStorage.getItem('username');
    const storedPassword = localStorage.getItem('password');
  
    return !!storedUsername && !!storedPassword;
}