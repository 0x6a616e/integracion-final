
import { push } from 'svelte-spa-router';

export const logout = () => {

    localStorage.removeItem('id');
    localStorage.removeItem('admin');
    localStorage.removeItem('token');

    push('/');
}