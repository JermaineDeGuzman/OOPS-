# Dictionary to store distances between various cities in the Philippines
destinations = {
    # Distances from Quezon City to other cities
    ("Quezon City", "Makati"): 12.5,
    ("Quezon City", "Pasig"): 10.2,
    ("Quezon City", "Manila"): 9.8,
    ("Quezon City", "Caloocan"): 6.9,
    ("Quezon City", "Taguig"): 13.1,
    ("Quezon City", "Pasay"): 12.7,
    ("Quezon City", "Mandaluyong"): 9.5,
    ("Quezon City", "San Juan"): 6.4,
    ("Quezon City", "Marikina"): 8.4,
    ("Quezon City", "Muntinlupa"): 21.2,
    ("Quezon City", "Las Piñas"): 20.3,
    ("Quezon City", "Parañaque"): 18.9,
    ("Quezon City", "Valenzuela"): 8.3,

    # Distances from Makati to other cities
    ("Makati", "Pasig"): 9.3,
    ("Makati", "Manila"): 6.5,
    ("Makati", "Caloocan"): 10.6,
    ("Makati", "Taguig"): 7.1,
    ("Makati", "Pasay"): 4.2,
    ("Makati", "Mandaluyong"): 4.1,
    ("Makati", "San Juan"): 6.0,
    ("Makati", "Marikina"): 11.4,
    ("Makati", "Muntinlupa"): 14.0,
    ("Makati", "Las Piñas"): 13.2,
    ("Makati", "Parañaque"): 10.7,
    ("Makati", "Valenzuela"): 13.5,

    # Distances from Pasig to other cities
    ("Pasig", "Manila"): 7.9,
    ("Pasig", "Caloocan"): 10.8,
    ("Pasig", "Taguig"): 7.2,
    ("Pasig", "Pasay"): 8.4,
    ("Pasig", "Mandaluyong"): 4.3,
    ("Pasig", "San Juan"): 5.2,
    ("Pasig", "Marikina"): 4.9,
    ("Pasig", "Muntinlupa"): 18.3,
    ("Pasig", "Las Piñas"): 17.2,
    ("Pasig", "Parañaque"): 14.8,
    ("Pasig", "Valenzuela"): 11.6,

    # Distances from Manila to other cities
    ("Manila", "Caloocan"): 11.8,
    ("Manila", "Taguig"): 9.3,
    ("Manila", "Pasay"): 5.6,
    ("Manila", "Mandaluyong"): 6.7,
    ("Manila", "San Juan"): 5.4,
    ("Manila", "Marikina"): 9.9,
    ("Manila", "Muntinlupa"): 18.8,
    ("Manila", "Las Piñas"): 17.4,
    ("Manila", "Parañaque"): 15.0,
    ("Manila", "Valenzuela"): 8.9,

    # Distances from Caloocan to other cities
    ("Caloocan", "Taguig"): 14.5,
    ("Caloocan", "Pasay"): 13.1,
    ("Caloocan", "Mandaluyong"): 9.6,
    ("Caloocan", "San Juan"): 7.8,
    ("Caloocan", "Marikina"): 10.5,
    ("Caloocan", "Muntinlupa"): 25.0,
    ("Caloocan", "Las Piñas"): 23.8,
    ("Caloocan", "Parañaque"): 21.3,
    ("Caloocan", "Valenzuela"): 6.3,

    # Distances from Taguig to other cities
    ("Taguig", "Pasay"): 8.6,
    ("Taguig", "Mandaluyong"): 6.0,
    ("Taguig", "San Juan"): 8.0,
    ("Taguig", "Marikina"): 10.3,
    ("Taguig", "Muntinlupa"): 12.4,
    ("Taguig", "Las Piñas"): 11.2,
    ("Taguig", "Parañaque"): 9.1,
    ("Taguig", "Valenzuela"): 14.6,

    # Distances from Pasay to other cities
    ("Pasay", "Mandaluyong"): 5.1,
    ("Pasay", "San Juan"): 6.9,
    ("Pasay", "Marikina"): 10.9,
    ("Pasay", "Muntinlupa"): 13.1,
    ("Pasay", "Las Piñas"): 11.9,
    ("Pasay", "Parañaque"): 9.2,
    ("Pasay", "Valenzuela"): 12.6,

    # Distances from Mandaluyong to other cities
    ("Mandaluyong", "San Juan"): 4.7,
    ("Mandaluyong", "Marikina"): 6.9,
    ("Mandaluyong", "Muntinlupa"): 16.3,
    ("Mandaluyong", "Las Piñas"): 15.1,
    ("Mandaluyong", "Parañaque"): 12.6,
    ("Mandaluyong", "Valenzuela"): 10.4,

    # Distances from San Juan to other cities
    ("San Juan", "Marikina"): 6.1,
    ("San Juan", "Muntinlupa"): 17.5,
    ("San Juan", "Las Piñas"): 16.3,
    ("San Juan", "Parañaque"): 13.8,
    ("San Juan", "Valenzuela"): 9.2,

    # Distances from Marikina to other cities
    ("Marikina", "Muntinlupa"): 19.2,
    ("Marikina", "Las Piñas"): 18.0,
    ("Marikina", "Parañaque"): 15.5,
    ("Marikina", "Valenzuela"): 10.1,

    # Distances from Muntinlupa to other cities
    ("Muntinlupa", "Las Piñas"): 10.0,
    ("Muntinlupa", "Parañaque"): 8.4,
    ("Muntinlupa", "Valenzuela"): 22.0,

    # Distances from Las Piñas to other cities
    ("Las Piñas", "Parañaque"): 7.2,
    ("Las Piñas", "Valenzuela"): 20.8,

    # Distance from Parañaque to Valenzuela
    ("Parañaque", "Valenzuela"): 18.3
}
