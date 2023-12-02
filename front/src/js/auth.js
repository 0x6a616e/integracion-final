
export const isAuthenticated = () => {
    const username = localStorage.getItem('id');
    const token = localStorage.getItem('token');
  
    return !!username && !!token;
}