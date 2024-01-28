//
//  KartControls.swift
//  MagnaKartaApp
//
//  Created by James on 27/01/2024.
//

import SwiftUI

struct KartControls: View {
    @Environment(MoveRepository.self) var repository
    
    var padding = 50.0
    
    @State var dragX: Double?
    @State var dragY: Double?
    
    var sizeX: Int?
    var sizeY: Int?
//    @State var isDragging = false
    
    var dragGesture: some Gesture {
        DragGesture(minimumDistance: 0)
            .onChanged { event in
                dragX = event.location.x
                dragY = event.location.y
                print(event.location)
                
                repository.move(x: dragX!, y: dragY!) { _ in }
            }
            .onEnded { _ in
                dragX = nil
                dragY = nil
//                isDragging = false
            }
    }
    
    var body: some View {
        GeometryReader { geo in
            HStack {
                Spacer()
                Image(systemName: "arrowshape.left.fill")
                Spacer()
                VStack {
                    Spacer()
                    Image(systemName: "arrowshape.up.fill")
                    Spacer()
                    Image(systemName: "arrowshape.down.fill")
                    Spacer()
                }
                .padding(.init(
                    top: padding,
                    leading: 0,
                    bottom: padding,
                    trailing: 0
                ))
                Spacer()
                Image(systemName: "arrowshape.right.fill")
                Spacer()
            }
            .onChange(of: dragY) {
                guard dragX != nil && dragY != nil else {
                    return
                }
                
                repository.move(x: dragX! / geo.size.width, y: dragY! / geo.size.height) {_ in}
            }
            .onChange(of: dragY) {
                guard dragX != nil && dragY != nil else {
                    return
                }
                
                repository.move(x: dragX! / geo.size.width, y: dragY! / geo.size.height) {_ in}
            }
        }
        .font(.system(size: 64))
        .aspectRatio(contentMode: .fit)
        .foregroundStyle(.white)
        .background(RoundedRectangle(cornerRadius: 25.0)
        .fill(.primary))
        .gesture(dragGesture)
        .shadow(radius: 10)
    }
}

#Preview {
    KartControls()
        .padding()
        .environment(MockMoveRepository() as MoveRepository)
}
