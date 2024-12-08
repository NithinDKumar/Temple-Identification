// src/services/templeService.js

import axios from 'axios';

const API_URL = 'http://localhost:5000/api/temple-details';

export const getTempleDetails = async (name, deity) => {
    try {
        const response = await axios.get(API_URL, {
            params: { name, deity }
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching temple details:', error);
        return null;
    }
};
