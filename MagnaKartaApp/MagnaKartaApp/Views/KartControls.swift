//
//  KartControls.swift
//  MagnaKartaApp
//
//  Created by James on 27/01/2024.
//

import SwiftUI

struct KartControls: View {
    var padding = 50.0
    
    @State var dragX: Double?
    @State var dragY: Double?
//    @State var isDragging = false
    
    var drag: some Gesture {
        DragGesture(minimumDistance: 0)
            .onChanged { event in
                dragX = event.location.x
                dragY = event.location.y
                print(event.location)
            }
            .onEnded { _ in
                dragX = nil
                dragY = nil
//                isDragging = false
            }
    }
    
    var body: some View {
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
        .font(.system(size: 64))
        .aspectRatio(contentMode: .fit)
        .foregroundStyle(.white)
        .background(RoundedRectangle(cornerRadius: 25.0)
            .fill(.primary))
        .gesture(drag)
        .shadow(radius: 10)
    }
}

#Preview {
    KartControls()
        .padding()
}
