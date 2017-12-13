import scala.io.Source
import scala.math.{abs, max}

object Day11 {


  def walk(steps: List[String], x: Int, y: Int, z: Int, max_distance: Int): (Int, Int) = {
    val distance =(abs(x) + abs(y) + abs(z)) / 2
      steps match {
      case Nil => (distance, max_distance)
      case head :: tail => {

        head match {
          case "s" => walk(tail, x, y - 1, z + 1, max(distance, max_distance))
          case "se" => walk(tail, x + 1, y - 1, z, max(distance, max_distance))
          case "sw" => walk(tail, x - 1, y, z + 1, max(distance, max_distance))
          case "n" => walk(tail, x, y + 1, z - 1, max(distance, max_distance))
          case "ne" => walk(tail, x + 1, y, z - 1, max(distance, max_distance))
          case "nw" => walk(tail, x - 1, y + 1, z, max(distance, max_distance))
        }
      }
    }
  }

  def main(args: Array[String]): Unit = {
    val fileContents = Source.fromFile("day11-input.txt").getLines.mkString
    val steps = fileContents.split(',')
    println(this.walk(steps.toList, 0, 0, 0, 0))
  }

}