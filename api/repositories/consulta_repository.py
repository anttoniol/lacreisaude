from api.repositories.repository import Repository


class ConsultaRepository(Repository):
    def save(self, data):
        cursor = self._db.cursor()
        query = "INSERT INTO coordinates (latitude, longitude, location_key) VALUES (%s, %s, %s)"
        values = (data["latitude"], data["longitude"], data["location_key"],)
        cursor.execute(query, values)

        self._db.commit()

        return {
            "row_id": cursor.lastrowid,
            "message": "Coordinates saved successfully!"
        }

    def save_if_not_exists(self, data):
        query_result = self.get_by_coordinates(data["latitude"], data['longitude'])

        if query_result is None:
            coordinates_data = {
                "latitude": data["latitude"],
                "longitude": data["longitude"],
                "location_key": data["location_key"]
            }
            insert_result = self.save(coordinates_data)
            return insert_result

        return {
            "row_id": query_result["id"],
            "message": "Coordinates obtained successfully!"
        }

    def get_by_id_profissional(self, id_profissional):
        cursor = self._db.cursor()
        query = ("SELECT name, initial_date, final_date, coordinates.latitude, coordinates.longitude, "
                 "forecast, coordinates.location_key FROM event INNER JOIN coordinates "
                 "ON event.coordinates_id = coordinates.id WHERE event.id = %s")
        values = (id_profissional,)

        cursor.execute(query, values)
        result = cursor.fetchone()

        if result is not None:
            return {
                "name": result[0],
                "initial_date": result[1],
                "final_date": result[2],
                "latitude": result[3],
                "longitude": result[4],
                "forecast": result[5],
                "location_key": result[6]
            }

        return None

    def update(self, id, data):
        result = self.__coordinates_repository.save_if_not_exists(data)

        cursor = self._db.cursor()

        query = ("UPDATE event SET name = %s, initial_date = %s, final_date = %s, coordinates_id = %s, "
                 "forecast = %s WHERE id = %s")
        values = (data["name"], data["initial_date"], data["final_date"], result["row_id"], data["forecast"], id,)

        cursor.execute(query, values)

        self._db.commit()

        return {
            "rows_affected": cursor.rowcount,
            "message": "Event updated successfully!"
        }

    def delete(self, id):
        cursor = self._db.cursor()

        sql = "DELETE FROM event WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self._db.commit()

        return {
            "rows_affected": cursor.rowcount,
            "message": "Event deleted successfully!"
        }
