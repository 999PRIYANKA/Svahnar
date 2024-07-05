import { useState, useEffect } from 'react';
import axios from 'axios';
import { useRouter } from 'next/router';

export default function ProductDetail() {
    const router = useRouter();
    const { id } = router.query;
    const [product, setProduct] = useState(null);

    useEffect(() => {
        if (id) {
            axios.get(`http://127.0.0.1:8000/api/products/${id}/`)
                .then(response => {
                    setProduct(response.data);
                })
                .catch(error => {
                    console.error(`There was an error fetching product ${id}`, error);
                });
        }
    }, [id]);

    if (!product) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>{product.name}</h1>
            <p>Price: ${product.price}</p>
            <p>Description: {product.description}</p>
        </div>
    );
}
