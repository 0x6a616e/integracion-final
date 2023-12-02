import axios from 'axios';
import {alertaExito} from './showAlert';
import {push } from 'svelte-spa-router';

export const getFunction = async (url) =>{
    const response = await axios.get(url);		
    return response.data.data;
}

export const postForm = async (url) => {
    const form = document.getElementById('form-product');
    const headers = {headers : {'Authorization' : `Bearer ${localStorage.getItem('token')}`} }  
    await axios.post(url , form, headers )
    .then( response =>{
        alertaExito();
        push('/');
    })
    .catch(error => {
        console.log(error)
    });
};

export const patchForm = async (url) =>{
    const form = document.getElementById('form-product');
    const headers = {headers : {'Authorization' : `Bearer ${localStorage.getItem('token')}`} }  
    await axios.patch(url, form, headers )
    .then( response =>{
        alertaExito();
        push('/');
    })
    .catch(error => {
        console.log(error)
    });
};

export const deleteData = async (url) => {
    const headers = {headers : {'Authorization' : `Bearer ${localStorage.getItem('token')}`} }  
    await axios.delete(url, headers )
    .then( response =>{
        alertaExito();
        push('/');
    })
    .catch(error => {
        console.log(error)
    });
};