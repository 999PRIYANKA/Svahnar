import { useState, useEffect } from 'react';
import axios from 'axios';

export default function Products() {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/products/')
            .then(response => {
                setProducts(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the products!', error);
            });
    }, []);

    return (
        <div>
            <h1>Product Catalog</h1>
            <ul>
                {products.map(product => (
                    <li key={product.id}>
                        {product.name} - ${product.price}
                        <a href={`/products/${product.id}`}>View Details</a>
                    </li>
                ))}
            </ul>
        </div>
    );
}
