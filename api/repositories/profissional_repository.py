from api.repositories.consulta_repository import ConsultaRepository
from api.repositories.repository import Repository


class ProfissionalRepository(Repository):
    def __init__(self):
        super().__init__()
        self.__coordinates_repository = ConsultaRepository()


    def save(self, data):
        result = self.__coordinates_repository.save_if_not_exists(data)

        cursor = self._db.cursor()
        query = ("INSERT INTO event (name, initial_date, final_date, coordinates_id, forecast) "
                 " VALUES (%s, %s, %s, %s, %s)")
        values = (data["name"], data["initial_date"], data["final_date"], result["row_id"], data["forecast"],)
        cursor.execute(query, values)

        self._db.commit()

        return {
            "row_id": cursor.lastrowid,
            "message": "Event saved successfully!"
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


    def get_by_coordinates(self, lat, lon):
        cursor = self._db.cursor()
        query = ("SELECT name, initial_date, final_date, coordinates.latitude, coordinates.longitude, "
                 "forecast, coordinates.location_key FROM event INNER JOIN coordinates ON "
                 "event.coordinates_id = coordinates.id WHERE coordinates.latitude = %s AND coordinates.longitude = %s")
        values = (lat, lon,)

        cursor.execute(query, values)
        results = cursor.fetchall()

        if results is not None:
            formatted_results = list()
            for result in results:
                formatted_results.append(
                    {
                        "name": result[0],
                        "initial_date": result[1],
                        "final_date": result[2],
                        "latitude": result[3],
                        "longitude": result[4],
                        "forecast": result[5],
                        "location_key": result[6]
                    }
                )
            return formatted_results

        return list()

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
